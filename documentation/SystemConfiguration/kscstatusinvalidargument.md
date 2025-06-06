# kSCStatusInvalidArgument

**Framework**: System Configuration  
**Kind**: var

An invalid argument was specified.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kSCStatusInvalidArgument: Int { get }
```

## See Also

- [var kSCStatusOK: Int](kscstatusok.md)
  The call was successful.
- [var kSCStatusFailed: Int](kscstatusfailed.md)
  A nonspecific failure occurred.
- [var kSCStatusAccessError: Int](kscstatusaccesserror.md)
  Permission is denied; you must be root to obtain a lock. As a result, the function could not create or access preferences.
- [var kSCStatusNoKey: Int](kscstatusnokey.md)
  No such key.
- [var kSCStatusKeyExists: Int](kscstatuskeyexists.md)
- [var kSCStatusLocked: Int](kscstatuslocked.md)
  A lock is already held.
- [var kSCStatusNeedLock: Int](kscstatusneedlock.md)
  A lock is required for this operation.
- [var kSCStatusNoStoreSession: Int](kscstatusnostoresession.md)
  The configuration daemon session is not active.
- [var kSCStatusNoStoreServer: Int](kscstatusnostoreserver.md)
  The configuration daemon is not available or no longer available.
- [var kSCStatusNotifierActive: Int](kscstatusnotifieractive.md)
  Notifier is currently active.
- [var kSCStatusNoPrefsSession: Int](kscstatusnoprefssession.md)
  The preferences session is not active.
- [var kSCStatusPrefsBusy: Int](kscstatusprefsbusy.md)
  A preferences update is currently in progress.
- [var kSCStatusNoConfigFile: Int](kscstatusnoconfigfile.md)
  The configuration file cannot be found.
- [var kSCStatusNoLink: Int](kscstatusnolink.md)
  No such link exists.
- [var kSCStatusStale: Int](kscstatusstale.md)
  A write was attempted on a stale version of the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/systemconfiguration/kscstatusinvalidargument)*