# formIndex(_:offsetBy:limitedBy:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

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
func formIndex(_ i: inout FlattenSequence<Base>.Index, offsetBy n: Int, limitedBy limit: FlattenSequence<Base>.Index) -> Bool
```

Available when `Base` conforms to `Collection` and `Base.Element` conforms to `Collection`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/flattensequence/formindex(_:offsetby:limitedby:))*