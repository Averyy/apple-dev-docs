# init(title:items:)

**Framework**: CarPlay  
**Kind**: init

Initializes the section with the specified title and items.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
init(title: String?, items: [CPMapPanelItem])
```

#### Return Value

An initialized section object.

## Parameters

- `title`: The localized title of the section. The system displays this string at the top of the section’s content. The section object stores a copy of the provided string. Specify `nil` if you don’t want to display a title for the section.
- `items`: The array of items to display in the section. Specify at least one item in this array. The section object stores a copy of the provided array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmappanelsection/init(title:items:))*