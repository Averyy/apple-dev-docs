# init(titleVariants:actions:)

**Framework**: CarPlay  
**Kind**: init

Creates an alert template.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
init(titleVariants: [String], actions: [CPAlertAction])
```

#### Return Value

A newly initialized alert template.

## Parameters

- `titleVariants`: An array of title variants. Each title should be localized and ready for display to the user. When the system displays the alert, it selects the title that best fits the available screen space, so arrange the variants from most to least preferred. Always include at least one title in the array.
- `actions`: An array of actions available on the alert. The array must contain at least one action.

## See Also

- [class var maximumActionCount: Int](cpalerttemplate/maximumactioncount.md)
  The maximum number of actions allowed in an alert template.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpalerttemplate/init(titlevariants:actions:))*