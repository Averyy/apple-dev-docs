# isSubclass(of:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns a Boolean value that indicates whether the receiving class is a subclass of, or identical to, a given class.

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
class func isSubclass(of aClass: AnyClass) -> Bool
```

#### Return Value

[`YES`](yes.md) if the receiving class is a subclass of—or identical to—`aClass`, otherwise [`NO`](no.md).

## Parameters

- `aClass`: A class object.

## See Also

- [class func superclass() -> AnyClass?](nsobject-swift.class/superclass.md)
  Returns the class object for the receiver’s superclass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/issubclass(of:))*