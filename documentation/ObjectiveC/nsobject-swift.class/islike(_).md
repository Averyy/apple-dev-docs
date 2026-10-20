# isLike(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the receiver is “like” another given object.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func isLike(_ object: String) -> Bool
```

```objc
- (BOOL) isLike:(NSString *) object;
```

#### Return Value

[`YES`](../yes.md) if the receiver is considered to be “like” `object`, otherwise [`NO`](../no.md).

#### Discussion

Currently, [`isLike(_:)`](./islike%28_%29.md) messages are never sent to any object from within Cocoa itself.

The default implementation for this method provided by `NSObject` method returns [`NO`](../no.md). `NSString` also provides an implementation of this method, which returns [`YES`](../yes.md) if the receiver matches a pattern described by `object`.

## Parameters

- `object`: The object with which to compare the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/islike(_:))*