# contactResolver

**Framework**: Core Spotlight  
**Kind**: property

A custom type you use to identify the owner of your app’s data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var contactResolver: (any ContactResolver)?
```

#### Discussion

Use this property to provide additional context about the person using your app. The model uses this information to help resolve first-person pronouns in prompts that indicate ownership of a particular data item. Provide any information about the person that makes sense for your app. For example, a communications app might include the person’s name and the phone number or email associated with their account.

For information about how to create a contact resolver, see [`Making your indexed content available to Foundation Models`](making-your-indexed-content-available-to-foundation-models.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/spotlightsearchtool/configuration-swift.struct/contactresolver)*