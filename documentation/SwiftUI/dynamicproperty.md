# DynamicProperty

**Framework**: SwiftUI  
**Kind**: protocol

An interface for a stored variable that updates an external property of a view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
protocol DynamicProperty
```

#### Overview

The view gives values to these properties prior to recomputing the view’s [`body`](view/body-8kl5o.md).

## Topics

### Updating the value
- [func update()](dynamicproperty/update.md)
  Updates the underlying value of the stored value.

## Relationships

### Conforming Types
- [AccessibilityFocusState](accessibilityfocusstate.md)
- [AppStorage](appstorage.md)
- [Binding](binding.md)
- [Environment](environment.md)
- [EnvironmentObject](environmentobject.md)
- [FetchRequest](fetchrequest.md)
- [FocusState](focusstate.md)
- [FocusedBinding](focusedbinding.md)
- [FocusedObject](focusedobject.md)
- [FocusedValue](focusedvalue.md)
- [GestureState](gesturestate.md)
- [NSApplicationDelegateAdaptor](nsapplicationdelegateadaptor.md)
- [Namespace](namespace.md)
- [ObservedObject](observedobject.md)
- [PhysicalMetric](physicalmetric.md)
- [ScaledMetric](scaledmetric.md)
- [SceneStorage](scenestorage.md)
- [SectionedFetchRequest](sectionedfetchrequest.md)
- [State](state.md)
- [StateObject](stateobject.md)
- [UIApplicationDelegateAdaptor](uiapplicationdelegateadaptor.md)
- [WKApplicationDelegateAdaptor](wkapplicationdelegateadaptor.md)
- [WKExtensionDelegateAdaptor](wkextensiondelegateadaptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dynamicproperty)*