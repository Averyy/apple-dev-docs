# init(rawValue:)

**Framework**: Core HID  
**Kind**: init

Creates a new instance with the specified raw value.

**Availability**:
- macOS 15.0+

## Declaration

```swift
init?(rawValue: UInt16)
```

#### Discussion

If there is no value of the type that corresponds with the specified raw value, this initializer returns `nil`. For example:

```None
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidusage/ledusage/init(rawvalue:))*