# Managing functions and function pointers

**Framework**: UIKit

Ensure that your code correctly handles functions, function pointers, and Objective-C messages.

#### Overview

The 64-bit runtime brings a number of changes in the calling and handling of functions. These changes affect how functions that accept a variable number of arguments and Objective-C messages are called in your code. Ensure that your code complies with these changes by adopting the calling conventions prescribed below.

##### Always Define Function Prototypes

When compiling using the updated project settings, the compiler generates errors if you attempt to make a function call to a function that doesn’t have an explicit prototype. You must provide a function prototype so that the compiler can determine whether or not the function is variadic.

##### Ensure That Function Pointers Use the Correct Prototype

If you pass a function pointer in your code, its calling conventions must take the same set of parameters everywhere in the code. Never cast a variadic function to a function that takes a fixed number of parameters (or vice versa).

The following code shows an example of a problematic function call:

```objc
int MyFunction(int a, int b, ...);

int (*action)(int, int, int) = (int (*)(int, int, int)) MyFunction;
action(1,2,3); // Incorrect.
```

Because the function pointer in this example is cast to use a different set of calling conventions, the calling function places the parameters in an order that the called function doesn’t expect. This behavior could cause your app to crash or to exhibit other unpredictable behaviors.

##### Call Variadic Functions with Consistent Types

Variadic functions are functions that contain variable argument lists (`varargs`). Variable arguments don’t provide type information. Furthermore, the arguments of variadic functions aren’t automatically promoted to larger types. In the 64-bit runtime, it’s important to understand this behavior if you pass in types of different sizes to variadic functions.

If you need to distinguish between different incoming data types, use a format string or other similar mechanism to provide that information to the `varargs` function. If the calling function doesn’t provide the right information (or if the `varargs` function doesn’t interpret it correctly), you get incorrect results.

For example, if your `varargs` function requires a `long` integer and you pass in a 32-bit value, the function contains 32 bits of the data you passed and 32 bits of data from the next argument. Likewise, if your `varargs` function requires an `int` type and you pass in a `long` integer, you get only half of the data. The remaining 32 bits of the data you pass appears in the argument that follows.

##### Cast Objective C Messages in Proper Form

If your code calls the [`objc_msgSend`](https://developer.apple.com/documentation/ObjectiveC/objc_msgSend) function, or any other similar functions in the Objective-C runtime that send messages, you need to cast properly. Although the prototype for the message functions has a variadic form, the method function that’s called by the Objective-C runtime doesn’t share the same prototype.

The Objective-C runtime directly calls the function that implements the method, so the calling conventions are mismatched. You must cast the [`objc_msgSend`](https://developer.apple.com/documentation/ObjectiveC/objc_msgSend) function to a prototype that matches the method function being called.

The following code shows proper form for dispatching a message to an object, using the low-level message functions:

```objc
- (int) doSomething:(int) x {
   return x + 2;
}

- (void) doSomethingElse {
    int (*action)(id, SEL, int) = (int (*)(id, SEL, int)) objc_msgSend;
    action(self, @selector(doSomething:), 0);
}
```

In this example, the `doSomething:` method takes a single parameter, `x`, and doesn’t have a variadic form. In `doSomethingElse`, it casts the [`objc_msgSend`](https://developer.apple.com/documentation/ObjectiveC/objc_msgSend) function using the prototype of the method function. Note that a method function always takes an `id` variable and a selector as its first two parameters. After the [`objc_msgSend`](https://developer.apple.com/documentation/ObjectiveC/objc_msgSend) function is cast to the function pointer named `action`, the call is dispatched through that same function pointer.

## See Also

- [Updating data structures](updating-data-structures.md)
  Review your app’s data design and update it to conform with 64-bit architecture.
- [Auditing pointer usage](auditing-pointer-usage.md)
  Ensure that the pointers in your code are safe for the 64-bit runtime.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/managing-functions-and-function-pointers)*