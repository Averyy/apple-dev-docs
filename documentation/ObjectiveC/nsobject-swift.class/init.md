# init()

**Framework**: Objective-C Runtime  
**Kind**: init

Implemented by subclasses to initialize a new object (the receiver) immediately after memory for it has been allocated.

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
init()
```

#### Return Value

An initialized object, or `nil` if an object could not be created for some reason that would not result in an exception.

#### Discussion

An [`init()`](nsobject-swift.class/init().md) message is coupled with an [`alloc`](nsobject-swift.class/alloc.md) (or [`allocWithZone:`](nsobject-swift.class/allocwithzone:.md)) message in the same line of code:

```objc
SomeClass *object = [[SomeClass alloc] init];
```

An object isn’t ready to be used until it has been initialized.

In a custom implementation of this method, you must invoke super’s [`Initialization`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Initialization.html#//apple_ref/doc/uid/TP40008195-CH21) then initialize and return the new object. If the new object can’t be initialized, the method should return `nil`. For example, a hypothetical `BuiltInCamera` class might return `nil` from its `init` method if run on a device that has no camera.

```objc
- (instancetype)init {
    if (self = [super init]) {
        // Initialize self
    }
    return self;
}
```

In some cases, a custom implementation of the [`init()`](nsobject-swift.class/init().md) method might return a substitute object. You must therefore always use the object returned by [`init()`](nsobject-swift.class/init().md), and not the one returned by [`alloc`](nsobject-swift.class/alloc.md) or [`allocWithZone:`](nsobject-swift.class/allocwithzone:.md), in subsequent code.

The [`init()`](nsobject-swift.class/init().md) method defined in the `NSObject` class does no initialization; it simply returns `self`. In terms of nullability, callers can assume that the `NSObject` implementation of [`init()`](nsobject-swift.class/init().md) does not return `nil`.

## See Also

- [func copy() -> Any](nsobject-swift.class/copy.md)
  Returns the object returned by `copy(with:)`.
- [func mutableCopy() -> Any](nsobject-swift.class/mutablecopy.md)
  Returns the object returned by `mutableCopy(with:)` where the zone is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/init())*