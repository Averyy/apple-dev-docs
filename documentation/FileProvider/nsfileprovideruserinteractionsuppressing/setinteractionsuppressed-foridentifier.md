# setInteractionSuppressed(_:forIdentifier:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Tells the File Provider extension that the user wants to suppress the user interaction.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func setInteractionSuppressed(_ suppression: Bool, forIdentifier suppressionIdentifier: String)
```

## Parameters

- `suppression`: A Boolean value that indicates whether the user wants to suppress the specified user interaction.
- `suppressionIdentifier`: A unique identifier for the user interaction.

## See Also

- [func isInteractionSuppressed(forIdentifier: String) -> Bool](nsfileprovideruserinteractionsuppressing/isinteractionsuppressed(foridentifier:).md)
  Asks the File Provider extension if the user suppressed the specified interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideruserinteractionsuppressing/setinteractionsuppressed(_:foridentifier:))*