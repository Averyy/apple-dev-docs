# Working with Core Foundation Types

**Framework**: Swift

Work directly with memory-managed Core Foundation types in your Swift code, and manually handle retains as needed.

#### Overview

When you import the Core Foundation framework, its types are imported as Swift classes. Wherever memory management annotations are provided, Swift automatically manages the memory of Core Foundation objects, including Core Foundation objects that you instantiate yourself. In Swift, you can use each pair of toll-free bridged Foundation and Core Foundation types interchangeably. You can also bridge some toll-free bridged Core Foundation types to Swift standard library types if you cast to a bridging Foundation type first. See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information.

##### Use Memory Managed Objects

When Swift imports Core Foundation types, the compiler remaps the names of these types. The compiler removes `Ref` from the end of each type name because all Swift classes are reference types; therefore, the suffix is redundant. The `CFTypeRef` type completely remaps to the `AnyObject` type.

Core Foundation objects returned from annotated APIs are automatically memory-managed in Swift—you don’t need to invoke the `CFRetain`, `CFRelease`, or `CFAutorelease` functions yourself.

If you return Core Foundation objects from your own C functions and Objective-C methods, you can annotate them with either the `CF_RETURNS_RETAINED` or `CF_RETURNS_NOT_RETAINED` macro to automatically insert memory management calls. You can also use the `CF_IMPLICIT_BRIDGING_ENABLED` and `CF_IMPLICIT_BRIDGING_DISABLED` macros to enclose C function declarations that follow the policy for Core Foundation ownership naming, in order to infer memory management.

##### Convert Unmanaged Objects to Memory Managed Objects

When Swift imports APIs that have not been annotated, the compiler cannot automatically memory-manage the returned Core Foundation objects. Swift wraps these returned Core Foundation objects in an [`Unmanaged`](unmanaged.md) structure. All indirectly returned Core Foundation objects are unmanaged as well. For example, here’s an unannotated C function:

```occ
CFStringRef StringByAddingTwoStrings(CFStringRef s1, CFStringRef s2)
```

And here’s how Swift imports it:

```swift
func StringByAddingTwoStrings(_: CFString!, _: CFString!) -> Unmanaged<CFString>! {
    // ...
}
```

When you receive an unmanaged object from an unannotated API, immediately convert it to a memory-managed object before you work with it. That way, Swift can handle memory management for you.

The `Unmanaged` structure provides two methods to convert an unmanaged object to a memory-managed object—`takeUnretainedValue()` and `takeRetainedValue()`. Both of these methods return the original, unwrapped type of the object. You choose which method to use based on whether the API you are invoking returns an unretained or a retained object.

For example, suppose the C function above doesn’t retain the `CFString` object before returning it. To start using the object, you use the `takeUnretainedValue()` function.

```swift
let memoryManagedResult = StringByAddingTwoStrings(str1, str2).takeUnretainedValue()
// memoryManagedResult is a memory managed CFString
```

You can also invoke the `retain()`, `release()`, and `autorelease()` methods on unmanaged objects, but this approach is not recommended.

For more information, see [`Ownership Policy`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148) in [`Memory Management Programming Guide for Core Foundation`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/CFMemoryMgmt.html#//apple_ref/doc/uid/10000127i).

## See Also

- [Working with Foundation Types](working-with-foundation-types.md)
  Use bridged Foundation types in your Swift codebase to work with dates, times, and other values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/working-with-core-foundation-types)*