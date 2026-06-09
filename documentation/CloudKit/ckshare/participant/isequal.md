# isEqual(_:)

**Framework**: CloudKit  
**Kind**: method

Compares two `CKShareParticipant` objects for person identity equality.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func isEqual(_ object: Any) -> Bool
```

#### Return Value

`YES` if both participants represent the same person, `NO` otherwise

#### Discussion

This implementation differs from typical `NSObject` `isEqual:` behavior. Standard `isEqual:` implementations compare all meaningful properties for structural equality. This method specifically compares identity to answer “Are these the same person?” rather than “Are these participant objects identical?”

This method returns `YES` if both participants represent the same person, regardless of differences in `role`, `acceptanceStatus`, `permission`, or other properties, or if CloudKit determines these represent the same identity via other heuristics.

The method returns `YES` if any of these identity conditions are met:

- `participantID` matches (direct participant identification)
- `userIdentity.userRecordID` matches (same CloudKit user)
- `userIdentity.lookupInfo` matches (same email, phone, or user record)

Properties NOT compared (may differ between “equal” participants):

- `role` (owner, privateUser, publicUser)
- `acceptanceStatus` (invited, accepted, removed, etc.)
- `permission` (readOnly, readWrite, none)
- `dateAddedToShare`
- `isApprovedRequester`

> ⚠️ **Warning**: Do not assume that participants returning `YES` from `isEqual:` have identical properties. Use explicit property comparisons when needed.

**Common use cases:**

Correct: Checking if person is already in share

```objc
if ([existingParticipants containsObject:newParticipant]) {
    // Person already exists in share (regardless of role/status)
}
```

Incorrect: Assuming structural equality

```objc
if ([participant1 isEqual:participant2]) {
    // DON'T assume participant1.role == participant2.role
    // DON'T assume same acceptanceStatus or permissions
}
```

Correct: Explicit structural comparison when needed

```objc
if ([participant1 isEqual:participant2] &&
    participant1.role == participant2.role &&
    participant1.acceptanceStatus == participant2.acceptanceStatus) {
    // Now you have both identity AND structural equality
}
```

## Parameters

- `object`: The object to compare against


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participant/isequal(_:))*