# formatted(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func formatted<S>(_ style: S) -> S.FormatOutput where Self == S.FormatInput, S : FormatStyle
```

## See Also

### Formatting a Sequence
- [func formatted() -> String](./formatted%28%29.md)
- [struct ListFormatStyle](../../Foundation/listformatstyle.md)
  A type that formats lists of items with a separator and conjunction appropriate for a given locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence/formatted(_:))*