# Equatable Implementations

**Framework**: App Intents

## Topics

### Operators
- [static func == (SyncableEntityIdentifier<LocalID, StableID>, SyncableEntityIdentifier<LocalID, StableID>) -> Bool](syncableentityidentifier/==(_:_:).md)
  Two identifiers are equal when they have the same shape **and** the same values: both-local compares local IDs (ignoring stable), both-stable-only compares stable IDs.  Mixed shapes (one has local, the other doesn’t) are never equal — this keeps the Hashable contract intact since each shape hashes a different component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/syncableentityidentifier/equatable-implementations)*