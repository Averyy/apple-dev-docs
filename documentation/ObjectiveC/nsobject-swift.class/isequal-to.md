# isEqual(to:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns a Boolean value that indicates whether the receiver is equal to another given object.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func isEqual(to object: Any?) -> Bool
```

#### Return Value

[`YES`](yes.md) if the receiver is equal to `object`, otherwise [`NO`](no.md). In effect returns [`NO`](no.md) if receiver is `nil`.

#### Discussion

During the evaluation of an `NSWhoseSpecifier` object that contains a test whose operator is `NSEqualToComparison`, an [`isEqual(to:)`](nsobject-swift.class/isequal(to:).md) message may be sent to each potentially specified object, if neither the potentially specified object nor the object being tested against implements a [`scriptingIsEqual(to:)`](nsobject-swift.class/scriptingisequal(to:).md) method.

The default implementation for this method provided by `NSObject` returns [`YES`](yes.md) if an `isEqualTo:` message sent to the same object would return [`YES`](yes.md).

## Parameters

- `object`: The object with which to compare the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isequal(to:))*