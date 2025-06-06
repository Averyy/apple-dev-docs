# displayedPerson

**Framework**: Address Book UI  
**Kind**: property

Optional. Specifies the person properties that the new-person view controller pre-fills in its views.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var displayedPerson: ABRecord? { get set }
```

#### Discussion

When this property has no person properties, the new-person view controller does not pre-fill properties in its views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbookui/abnewpersonviewcontroller/displayedperson)*