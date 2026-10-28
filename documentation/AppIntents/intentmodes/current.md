# IntentModes.Current

**Framework**: App Intents  
**Kind**: struct  
**Role**: Structure

The current runtime behavior of an app intent.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Current
```

## Overview

This type provides information about an app intent’s current runtime behavior. When an intent runs, its [`systemContext`](../appintent/systemcontext.md) property contains additional contextual information you can use to make decisions. Specifically, the [`currentMode`](../intentsystemcontext/currentmode.md) property tells you whether the intent is currently running in the foreground or background.

Don’t create instances of this type yourself. Instead, compare the value in the [`currentMode`](../intentsystemcontext/currentmode.md) property to the static values this type defines. You can also check the [`canContinueInForeground`](./current/cancontinueinforeground.md) property to determine if a background intent can switch to the foreground. The following code shows how to use this type from an app intent’s [`perform()`](../appintent/perform%28%29.md) method:

```swift
if systemContext.currentMode == .background {
   if systemContext.currentMode.canContinueInForeground {
      try await continueInForeground()
   } else {
      // The current conditions don't allow the app intent to continue in the foreground,
      // so it needs to continue in the background.
   }
}
```

## Topics

### Instance Properties
- [var canContinueInForeground: Bool](./current/cancontinueinforeground.md)
  A Boolean value that indicates whether running the app intent in the foreground is possible.
### Type Properties
- [static var background: IntentModes.Current](./current/background.md)
  A value that indicates the app intent is running in the background.
- [static var foreground: IntentModes.Current](./current/foreground.md)
  A value that indicates the app intent is running in the foreground.

## Relationships

### Conforms To
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentmodes/current)*