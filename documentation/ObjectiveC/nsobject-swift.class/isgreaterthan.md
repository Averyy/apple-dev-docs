# isGreaterThan(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns a Boolean value that indicates whether the receiver is greater than another given object.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func isGreaterThan(_ object: Any?) -> Bool
```

#### Return Value

[`YES`](yes.md) if the receiver is greater than `object`, otherwise [`NO`](no.md).

#### Discussion

During the evaluation of an `NSWhoseSpecifier` object that contains a test whose operator is `NSGreaterThanComparison`, an [`isGreaterThan(_:)`](nsobject-swift.class/isgreaterthan(_:).md) message may be sent to each potentially specified object, if the potentially specified object does not implement a [`scriptingIsGreaterThan(_:)`](nsobject-swift.class/scriptingisgreaterthan(_:).md) method and the object being tested against does not implement a [`scriptingIsLessThanOrEqual(to:)`](nsobject-swift.class/scriptingislessthanorequal(to:).md) method.

The default implementation for this method provided by `NSObject` returns [`YES`](yes.md) if a `compare:` message sent to the same object would return `NSOrderedDescending`.

## Parameters

- `object`: The object with which to compare the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isgreaterthan(_:))*