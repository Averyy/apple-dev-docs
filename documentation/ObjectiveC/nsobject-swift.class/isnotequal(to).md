# isNotEqual(to:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the receiver is not equal to another given object.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func isNotEqual(to object: Any?) -> Bool
```

```objc
- (BOOL) isNotEqualTo:(id) object;
```

## Return Value

[`YES`](../yes.md) if the receiver is not equal to `object`, otherwise [`NO`](../no.md).

## Discussion

Currently, [`isNotEqual(to:)`](./isnotequal%28to%29.md) messages are never sent to any object from within Cocoa itself.

The default implementation for this method provided by `NSObject` method returns [`YES`](../yes.md) if an `isEqual:` message sent to the same object would return [`NO`](../no.md).

## Parameters

- `object`: The object with which to compare the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isnotequal(to:))*