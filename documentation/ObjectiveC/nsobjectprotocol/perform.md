# perform(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Required**: Yes

Sends a specified message to the receiver and returns the result of the message.

**Availability**:
- iOS 1.0+
- iPadOS 1.0+
- Mac Catalyst 1.0+
- macOS 10.0+
- tvOS 1.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func perform(_ aSelector: Selector!) -> Unmanaged<AnyObject>!
```

#### Return Value

An object that is the result of the message.

#### Discussion

Calling the [`perform(_:)`](nsobjectprotocol/perform(_:).md) method is equivalent to sending the `aSelector` message directly to the receiver. For example, the following both do the same thing if `anObject` is an instance of `MyObject`:

The [`perform(_:)`](nsobjectprotocol/perform(_:).md) method allows you to send messages that aren’t determined until run-time. This means that you can pass a variable selector as the argument:

Use caution when doing this. This method returns an implicitly unwrapped optional unmanaged pointer to an `AnyObject` instance ([`Unmanaged`](https://developer.apple.com/documentation/Swift/Unmanaged)`<`[`AnyObject`](https://developer.apple.com/documentation/Swift/AnyObject)`>!`).  It’s up to you to decide how to bring the instance into Swift’s memory management scheme.  Different messages require different memory management strategies for their returned objects, and it might not be obvious which to use.

Usually, a caller isn’t responsible for the memory of a returned instance, in which case you use [`takeUnretainedValue()`](https://developer.apple.com/documentation/Swift/Unmanaged/takeUnretainedValue()), as shown above. However, for any of the creation methods, such as [`copy()`](nsobject-swift.class/copy().md), the caller is responsible, and you use [`takeRetainedValue()`](https://developer.apple.com/documentation/Swift/Unmanaged/takeRetainedValue()) instead. See [`Memory Management Policy`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/mmRules.html#//apple_ref/doc/uid/20000994) in [`Advanced Memory Management Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i) for a description of ownership expectations.

Due to this uncertainty, the compiler generates a warning if you supply a variable selector while using ARC to manage memory. Because it can’t determine ownership of the returned object at compile-time, ARC makes the assumption that the caller does  need to take ownership, but this may not be true. The compiler warning alerts you to the potential for a memory leak.

To avoid the warning, if you know that `aSelector` has no return value, you might be able to use [`performSelector(onMainThread:with:waitUntilDone:)`](nsobject-swift.class/performselector(onmainthread:with:waituntildone:).md) or one of the related methods available in [`NSObject`](nsobject-swift.class.md).

For a more general solution, use [`NSInvocation`](https://developer.apple.com/documentation/Foundation/NSInvocation) to construct a message that you can invoke with an arbitrary argument list and return value.

Alternatively, consider restructuring your code to use blocks as a means of passing chunks of functionality through an API. See [`Blocks Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Blocks/Articles/00_Introduction.html#//apple_ref/doc/uid/TP40007502) for details.

> ❗ **Important**:  Because of the inherent lack of type safety, this API isn’t recommended for use in Swift unless your code specifically relies on the dynamic method resolution provided by the Objective-C run-time. For more information about using selectors in Swift and alternatives to the [`perform(_:)`](nsobjectprotocol/perform(_:).md) function, read [`Using Objective-C Runtime Features in Swift`](https://developer.apple.com/documentation/Swift/using-objective-c-runtime-features-in-swift).

 Because of the inherent lack of type safety, this API isn’t recommended for use in Swift unless your code specifically relies on the dynamic method resolution provided by the Objective-C run-time.

For more information about using selectors in Swift and alternatives to the [`perform(_:)`](nsobjectprotocol/perform(_:).md) function, read [`Using Objective-C Runtime Features in Swift`](https://developer.apple.com/documentation/Swift/using-objective-c-runtime-features-in-swift).

## Parameters

- `aSelector`: A selector identifying the message to send. The message should take no arguments. If   is  , an   is raised.

## See Also

- [func perform(Selector!, with: Any!) -> Unmanaged<AnyObject>!](nsobjectprotocol/perform(_:with:).md)
  Sends a message to the receiver with an object as the argument.
- [func perform(Selector!, with: Any!, with: Any!) -> Unmanaged<AnyObject>!](nsobjectprotocol/perform(_:with:with:).md)
  Sends a message to the receiver with two objects as arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobjectprotocol/perform(_:))*