# readLine(strippingNewline:)

**Framework**: Swift  
**Kind**: func

Returns a string read from standard input through the end of the current line or until EOF is reached.

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
func readLine(strippingNewline: Bool = true) -> String?
```

#### Return Value

The string of characters read from standard input. If EOF has already been reached when `readLine()` is called, the result is `nil`.

#### Discussion

Standard input is interpreted as `UTF-8`. Invalid bytes are replaced by Unicode [`replacement characters`](https://developer.apple.comhttps://unicode.org/glossary/#replacement_character).

## Parameters

- `strippingNewline`: If  , newline characters and character   combinations are stripped from the result; otherwise, newline characters   or character combinations are preserved. The default is  .

## See Also

- [enum CommandLine](commandline.md)
  Command-line arguments for the current process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/readline(strippingnewline:))*