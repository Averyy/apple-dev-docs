# isLessThan(_:)

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the receiver is less than another given object.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
func isLessThan(_ object: Any?) -> Bool
```

```objc
- (BOOL) isLessThan:(id) object;
```

#### Return Value

[`YES`](../yes.md) if the receiver is less than `object`, otherwise [`NO`](../no.md).

#### Discussion

During the evaluation of an `NSWhoseSpecifier` object that contains a test whose operator is `NSLessThanComparison`, an [`isLessThan(_:)`](./islessthan%28_%29.md) message may be sent to each potentially specified object, if the potentially specified object does not implement a [`scriptingIsLessThan(_:)`](./scriptingislessthan%28_%29.md) method and the object being tested against does not implement a [`scriptingIsGreaterThanOrEqual(to:)`](./scriptingisgreaterthanorequal%28to%29.md) method.

The default implementation for this method provided by `NSObject` method returns [`YES`](../yes.md) if a `compare:` message sent to the same object would return `NSOrderedAscending`.

## Parameters

- `object`: The object with which to compare the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/islessthan(_:))*