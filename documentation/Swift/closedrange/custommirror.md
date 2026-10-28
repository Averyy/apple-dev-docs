# customMirror

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

The custom mirror for this instance.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var customMirror: Mirror { get }
```

Available when `Bound` conforms to `Comparable`.

## Discussion

If this type has value semantics, the mirror should be unaffected by subsequent mutations of the instance.

## See Also

### Describing a Range
- [var description: String](./description.md)
  A textual representation of the range.
- [var debugDescription: String](./debugdescription.md)
  A textual representation of the range, suitable for debugging.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/closedrange/custommirror)*