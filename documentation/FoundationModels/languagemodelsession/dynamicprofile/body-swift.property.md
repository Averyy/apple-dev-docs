# body

**Framework**: Foundation Models  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The content of the dynamic profile.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@LanguageModelSession
.DynamicProfileBuilder var body: Self.Body { get }
```

## See Also

### Implementing a dynamic profile
- [associatedtype Body : LanguageModelSession.DynamicProfile](./body-swift.associatedtype.md)
  The type of dynamic profile that represent this profile.
- [LanguageModelSession.DynamicProfile.DynamicProfile](./dynamicprofile.md)
  The dynamic profile type that a dynamic profile’s body composes.
- [LanguageModelSession.DynamicProfile.Profile](./profile.md)
  The profile type that a dynamic profile activates.
- [LanguageModelSession.DynamicProfile.SessionProperty](./sessionproperty.md)
  A property wrapper that provides access to a session property from within a dynamic profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/dynamicprofile/body-swift.property)*