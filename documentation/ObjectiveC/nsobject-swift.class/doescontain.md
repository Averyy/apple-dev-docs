# doesContain(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns a Boolean value that indicates whether the receiver contains a given object.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func doesContain(_ object: Any) -> Bool
```

#### Return Value

[`YES`](yes.md) if the receiver contains `object`, otherwise [`NO`](no.md).

#### Discussion

Currently, [`doesContain(_:)`](nsobject-swift.class/doescontain(_:).md) messages are never sent to any object from within Cocoa itself.

The default implementation for this method provided by `NSObject` returns [`YES`](yes.md) if the receiver is actually an `NSArray` object and an [`indexOfObjectIdentical(to:)`](https://developer.apple.com/documentation/foundation/nsarray/1410847-indexofobjectidentical) message sent to the same object would return something other than `NSNotFound`.

## Parameters

- `object`: The object to search for in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/doescontain(_:))*