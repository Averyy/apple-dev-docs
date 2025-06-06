# stopAccessingSecurityScopedResource()

**Framework**: Foundation  
**Kind**: method

Revokes the access granted to the url by a prior successful call to the complementary start function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func stopAccessingSecurityScopedResource()
```

## Mentions

- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)

#### Discussion

When you no longer need access to a file or directory pointed to by a security-scoped URL, such as one returned by resolving a security-scoped bookmark, call this method on the URL to relinquish access. You can also use its Core Foundation equivalent, the [`CFURLStopAccessingSecurityScopedResource(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFURLStopAccessingSecurityScopedResource(_:)) function.

You must balance each call to [`startAccessingSecurityScopedResource()`](url/startaccessingsecurityscopedresource().md) for a given security-scoped URL with a call to [`stopAccessingSecurityScopedResource()`](url/stopaccessingsecurityscopedresource().md). When you make the last balanced call to [`stopAccessingSecurityScopedResource()`](url/stopaccessingsecurityscopedresource().md), you immediately lose access to the resource in question.

> ⚠️ **Warning**:  If you fail to relinquish your access to file-system resources when you no longer need them, your app leaks kernel resources. If sufficient kernel resources leak, your app loses its ability to add file-system locations to its sandbox, such as with Powerbox or security-scoped bookmarks, until relaunched.

 If you fail to relinquish your access to file-system resources when you no longer need them, your app leaks kernel resources. If sufficient kernel resources leak, your app loses its ability to add file-system locations to its sandbox, such as with Powerbox or security-scoped bookmarks, until relaunched.

If you call this method on a URL whose referenced resource you don’t have access to, nothing happens.

> **Note**:  Security-scoped bookmarks aren’t available in versions of macOS prior to OS X 10.7.3.

 Security-scoped bookmarks aren’t available in versions of macOS prior to OS X 10.7.3.

## See Also

- [func startAccessingSecurityScopedResource() -> Bool](url/startaccessingsecurityscopedresource.md)
  Given a url created by resolving a bookmark data created with security scope, make the resource referenced by the url accessible to the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/url/stopaccessingsecurityscopedresource())*