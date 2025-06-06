# localizedString(forLabel:)

**Framework**: Contacts  
**Kind**: method

Returns a localized string for the specified label.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func localizedString(forLabel label: String) -> String
```

#### Return Value

Returns a localized string for the label.

#### Discussion

All predefined label constants are localized and this method returns their localized strings. A custom label will be returned as is, so this method can be used to convert all labels for display.

## Parameters

- `label`: The label to be localized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnlabeledvalue/localizedstring(forlabel:))*