# prepareProtectionClasses(_:)

**Framework**: Core Spotlight  
**Kind**: method

Performs one-time tasks that prepare Spotlight to search for content in one or more protected search indexes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
class func prepareProtectionClasses(_ protectionClasses: [FileProtectionType])
```

#### Discussion

Call this method once during your app’s lifecycle to give Spotlight time to load the resources it needs for search. This method prepares only the indexes that have the specified protetction levels. This preparation comes at a cost, so measure your app’s performance and determine an appropriate time to call it. For example, you might call it when you load an interface that includes search features.

You don’t need to call this method more than once during the lifetime of your app, but it’s safe to call the method multiple times.

## Parameters

- `protectionClasses`: The file protection types associated with the indexes you plan to search.

## See Also

- [class func prepare()](csuserquery/prepare.md)
  Performs one-time tasks that prepare Spotlight to search for content in all search indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquery/prepareprotectionclasses(_:))*