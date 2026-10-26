# PHPickerConfigurationSelection.ordered

**Framework**: PhotosUI  
**Kind**: case  
**Role**: Case

An option that provides selected photos to the app in the chosen order after the user confirms the selection.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
case ordered
```

```c
PHPickerConfigurationSelectionOrdered
```

#### Discussion

This option notifies the app of photo selections when a person taps the Add button.

In addition, selected photos display a numbered badge that represents the order in which someone taps the photo.

## See Also

### Selection methods
- [PHPickerConfigurationSelection.default](./default.md)
  An option that provides selected photos to the app in the default order after the user confirms the selection.
- [PHPickerConfigurationSelection.continuous](./continuous.md)
  An option that provides the app a person’s selection immediately.
- [PHPickerConfigurationSelection.continuousAndOrdered](./continuousandordered.md)
  An option that provides the app a person’s selection immediately and displays selected photos with a numbered badge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerconfigurationselection/ordered)*