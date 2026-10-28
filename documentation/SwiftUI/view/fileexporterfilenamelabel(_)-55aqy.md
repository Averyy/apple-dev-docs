# fileExporterFilenameLabel(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

On macOS, configures the `fileExporter` with a label for the file name field.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func fileExporterFilenameLabel(_ labelKey: LocalizedStringKey) -> some View
```

**Other overloads**:

```swift
@export(implementation)
nonisolated func fileExporterFilenameLabel(_ label: LocalizedStringResource) -> some View
```

```swift
nonisolated
func fileExporterFilenameLabel(_ label: Text?) -> some View
```

```swift
nonisolated
func fileExporterFilenameLabel<S>(_ label: S) -> some View where S : StringProtocol
```

## Parameters

- `labelKey`: The key to a localized string to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/fileexporterfilenamelabel(_:)-55aqy)*