# PHPickerConfigurationSelection.continuousAndOrdered

**Framework**: PhotosUI  
**Kind**: case  
**Role**: Case

An option that provides the app a person’s selection immediately and displays selected photos with a numbered badge.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case continuousAndOrdered
```

```c
PHPickerConfigurationSelectionContinuousAndOrdered
```

#### Discussion

This option notifies the app of photo selections dynamically, as someone taps the photo picker.

In addition, selected photos display a numbered badge that represents the order in which someone taps the photo.

## See Also

### Selection methods
- [PHPickerConfigurationSelection.default](./default.md)
  An option that provides selected photos to the app in the default order after the user confirms the selection.
- [PHPickerConfigurationSelection.ordered](./ordered.md)
  An option that provides selected photos to the app in the chosen order after the user confirms the selection.
- [PHPickerConfigurationSelection.continuous](./continuous.md)
  An option that provides the app a person’s selection immediately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfigurationselection/continuousandordered)*