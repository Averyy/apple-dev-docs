# SRStateReporter

**Framework**: StateReporting  
**Kind**: class  
**Role**: Class

An object unique per domain that records state transitions and volatile metadata updates.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```objc
@interface SRStateReporter : NSObject
```

## Overview

`SRStateReporter` is the central object for recording your feature’s or subsystem’s current state. Obtain an instance through the [`reporterForDomain:`](./srstatereporter/reporterfordomain_.md) method, which guarantees that every caller using the same domain string receives the same object.

A state is uniquely identified by its label and stable metadata. A transition to a new state occurs when the label or stable metadata changes; reporting the same label and stable metadata as the current state is a no-op. *Volatile metadata* provides additional context within an ongoing state and is discarded when the next transition begins. Context dictionaries must contain only `NSNumber`, `NSString`, or `NSDate` values.

Call [`reportTransitionToStateLabel:stableMetadata:volatileMetadata:`](./srstatereporter/reporttransitiontostatelabel_stablemetadata_volatilemetadata_.md) whenever your feature transitions to a new state. Pass `nil` as the label to signal that no state is active. Call [`reportVolatileMetadataUpdate:`](./srstatereporter/reportvolatilemetadataupdate_.md) to update volatile metadata without beginning a new state transition. Calling either method more frequently than user interaction timescales can trigger rate limiting, causing state updates to go unlogged.

```objc
SRStateReporter *reporter =
    [SRStateReporter reporterForDomain:@"com.example.myapp.checkout"];

[reporter reportTransitionToStateLabel:@"paymentSheet"
                 stableMetadata:@{@"userTier": @"premium"}
                volatileMetadata:@{@"cartTotal": @(49.99)}];
```

For Swift, use [`StateReporter`](./statereporter.md).

## Topics

### Instance Properties
- [domain](./srstatereporter/domain.md)
  The reverse DNS-style domain name that identifies this reporter.
### Instance Methods
- [- reportTransitionToStateLabel:stableMetadata:volatileMetadata:](./srstatereporter/reporttransitiontostatelabel_stablemetadata_volatilemetadata_.md)
  Reports a transition to a new state.
- [- reportVolatileMetadataUpdate:](./srstatereporter/reportvolatilemetadataupdate_.md)
  Updates the volatile metadata within the current state without beginning a new transition.
### Type Methods
- [+ reporterForDomain:](./srstatereporter/reporterfordomain_.md)
  Returns the reporter instance unique to the given domain name.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/statereporting/srstatereporter)*