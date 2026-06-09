# SynchronizationTokens

**Framework**: Device Management  
**Kind**: dictionary

The server’s synchronization token.

## Declaration

```swift
object SynchronizationTokens
```

## Mentions

- [Integrating declarative management](integrating-declarative-management.md)

## Properties

- `DeclarationsToken` (string) *(required)*: The synchronization token for declarations.
- `Timestamp` (date-time) *(required)*: The timestamp for the creation of the set of sync tokens. Clients use this to determine the most recent set of sync tokens when different sources provide the tokens. Use the format `YYYY-mm-ddTHH:MM:SSZ`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/synchronizationtokens)*