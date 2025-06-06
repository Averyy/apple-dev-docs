# init(rawValue:)

**Framework**: FamilyControls  
**Kind**: init

Creates a new instance with the specified raw value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
init?(rawValue: Int)
```

#### Discussion

If there is no value of the type that corresponds with the specified raw value, this initializer returns `nil`. For example:

```swift
enum PaperSize: String {
    case A4, A5, Letter, Legal
}

print(PaperSize(rawValue: "Legal"))
// Prints "Optional(PaperSize.Legal)"

print(PaperSize(rawValue: "Tabloid"))
// Prints "nil"
```

## Parameters

- `rawValue`: The raw value to use for the new instance.

## See Also

- [init(from: any Decoder) throws](authorizationstatus/init(from:).md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/authorizationstatus/init(rawvalue:))*