# isGreaterThanOrEqual(to:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the receiver is greater than or equal to another given object.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func isGreaterThanOrEqual(to object: Any?) -> Bool
```

```objc
- (BOOL) isGreaterThanOrEqualTo:(id) object;
```

## Return Value

[`YES`](../yes.md) if the receiver is greater than or equal to `object`, otherwise [`NO`](../no.md).

## Discussion

During the evaluation of an `NSWhoseSpecifier` object that contains a test whose operator is `NSGreaterThanOrEqualToComparison`, an[`isGreaterThanOrEqual(to:)`](./isgreaterthanorequal%28to%29.md) message may be sent to each potentially specified object, if the potentially specified object does not implement a [`scriptingIsGreaterThanOrEqual(to:)`](./scriptingisgreaterthanorequal%28to%29.md) method and the object being tested against does not implement a [`scriptingIsLessThan(_:)`](./scriptingislessthan%28_%29.md) method.

The default implementation for this method provided by `NSObject` returns [`YES`](../yes.md) if a `compare:` message sent to the same object would return `NSOrderedSame` or `NSOrderedDescending`.

## Parameters

- `object`: The object with which to compare the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/isgreaterthanorequal(to:))*