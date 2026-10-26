# init(title:identifier:subtitle:selected:requiredOptionsIdentifiers:)

**Framework**: SharedWithYouCore  
**Kind**: init  
**Role**: Initializer

Creates and initializes a collaboration option object with the provided values.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
convenience init(title: String, identifier: String, subtitle: String = "", selected: Bool = false, requiredOptionsIdentifiers: [String] = [])
```

## Parameters

- `title`: A localized string the system displays as a title.
- `identifier`: A unique identifier.
- `subtitle`: A localized string the system displays as a subtitle.
- `selected`: A Boolean value that represents the selected state of an option.
- `requiredOptionsIdentifiers`: An array of option identifiers.

## See Also

### Creating collaboration options
- [init(title: String, identifier: String)](./init%28title,identifier%29.md)
  Creates and initializes a collaboration option object with a provided title and identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationoption/init(title:identifier:subtitle:selected:requiredoptionsidentifiers:))*