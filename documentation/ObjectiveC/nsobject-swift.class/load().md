# load()

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Type Method

Invoked whenever a class or category is added to the Objective-C runtime; implement this method to perform class-specific behavior upon loading.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func load()
```

```objc
+ (void) load;
```

#### Discussion

The [`load()`](./load%28%29.md) message is sent to classes and categories that are both dynamically loaded and statically linked, but only if the newly loaded class or category implements a method that can respond.

The order of initialization is as follows:

1. All initializers in any framework you link to.
2. All `+load` methods in your image.
3. All C++ static initializers and C/C++ `__attribute__(constructor)` functions in your image.
4. All initializers in frameworks that link to you.

In addition:

- A class’s `+load` method is called after all of its superclasses’ `+load` methods.
- A category `+load` method is called after the class’s own `+load` method.

In a custom implementation of [`load()`](./load%28%29.md) you can therefore safely message other unrelated classes from the same image, but any [`load()`](./load%28%29.md) methods implemented by those classes may not have run yet.

> ❗ **Important**:  Custom implementations of the `load` method for Swift classes bridged to Objective-C are not called automatically.

## See Also

### Initializing a Class
- [class func initialize()](./initialize%28%29.md)
  Initializes the class before it receives its first message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/load())*