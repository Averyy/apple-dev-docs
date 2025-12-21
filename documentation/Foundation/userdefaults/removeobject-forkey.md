# removeObject(forKey:)

**Framework**: Foundation  
**Kind**: method

Removes the value for the specified key from the defaults database.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeObject(forKey defaultName: String)
```

#### Discussion

This method removes the specified key and value from the app-specific settings. If your `UserDefaults` object writes to settings for an app group or other shared settings file, the method removes the key from that file instead. This method removes the key and value only from the target domain, and doesn’t impact values for the same key in other domains. For example, it doesn’t remove keys and values from the global domain.

After you remove the key, the system generates a [`didChangeNotification`](userdefaults/didchangenotification.md) for registered observers.

## Parameters

- `defaultName`: The key with the value you want to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/removeobject(forkey:))*