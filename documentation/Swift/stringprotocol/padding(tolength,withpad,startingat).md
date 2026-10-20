# padding(toLength:withPad:startingAt:)

**Framework**: Swift  
**Kind**: method

Returns a new string formed from the `String` by either removing characters from the end, or by appending as many occurrences as necessary of a given pad string.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func padding<T>(toLength newLength: Int, withPad padString: T, startingAt padIndex: Int) -> String where T : StringProtocol
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/stringprotocol/padding(tolength:withpad:startingat:))*