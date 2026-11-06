# authenticationPolicy

**Framework**: App Intents  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

The authentication policy to enforce when the system accesses this entity.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
static var authenticationPolicy: IntentAuthenticationPolicy { get }
```

## Discussion

This is the minimum policy for each of the entity’s properties. A property’s own `authenticationPolicy` can make it stricter; a weaker one is raised to this policy. The default value of this property is [`IntentAuthenticationPolicy.alwaysAllowed`](../intentauthenticationpolicy/alwaysallowed.md).

## Default Implementations

### AppEntity Implementations
- [static var authenticationPolicy: IntentAuthenticationPolicy](./authenticationpolicy-63wt1.md)
  The authentication policy to enforce when the system accesses this entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appentity/authenticationpolicy)*