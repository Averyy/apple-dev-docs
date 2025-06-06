# hasSuffix(_:)

**Framework**: Swift  
**Kind**: method

Returns a Boolean value indicating whether the string ends with the specified suffix.

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
func hasSuffix<Suffix>(_ suffix: Suffix) -> Bool where Suffix : StringProtocol
```

#### Return Value

`true` if the string ends with `suffix`; otherwise, `false`.

#### Discussion

The comparison is both case sensitive and Unicode safe. The case-sensitive comparison will only match strings whose corresponding characters have the same case.

```swift
let plans = "Let's meet at the café"

// Case sensitive
print(plans.hasSuffix("Café"))
// Prints "false"
```

The Unicode-safe comparison matches Unicode extended grapheme clusters rather than the code points used to compose them. The example below uses two strings with different forms of the `"é"` character—the first uses the composed form and the second uses the decomposed form.

```swift
// Unicode safe
let composedCafe = "café"
let decomposedCafe = "cafe\u{0301}"

print(plans.hasSuffix(composedCafe))
// Prints "true"
print(plans.hasSuffix(decomposedCafe))
// Prints "true"
```

## Parameters

- `suffix`: A possible suffix to test against this string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/hassuffix(_:))*