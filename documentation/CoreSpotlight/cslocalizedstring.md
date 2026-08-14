# CSLocalizedString

**Framework**: Core Spotlight  
**Kind**: class

An object that displays localized text in search results related to your app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class CSLocalizedString
```

#### Overview

The `CSLocalizedString` class helps you localize text in searchable items. You can use a `CSLocalizedString` object in place of an [`NSString`](https://developer.apple.com/documentation/foundation/nsstring) object to display localized text in search results related to your app.

For example, you might use the following code to define a `CSLocalizedString` object for a searchable item you want to identify as “Song” in English:

```objc
CSSearchableItem *item = [CSSearchableItem new];
    item.uniqueIdentifier = @"song";
 
    CSSearchableItemAttributeSet *attributes = [[CSSearchableItemAttributeSet alloc] initWithItemContentType:(NSString *)kUTTypeItem];
    item.attributeSet = attributes;
 
    CSLocalizedString *displayName = [[CSLocalizedString alloc] initWithLocalizedStrings:@{@"en":@"Song", @"fr":@"Chanson"}];
    attributes.displayName = displayName.localizedString;
```

## Topics

### Specifying localized strings
- [init(localizedStrings: [AnyHashable : Any])](cslocalizedstring/init(localizedstrings:).md)
  Initializes a `CSLocalizedString` object with the specified dictionary of localized strings.
### Getting a localized string
- [func localizedString() -> String](cslocalizedstring/localizedstring.md)
  Returns the localized string for the current language.

## Relationships

### Inherits From
- [NSString](../foundation/nsstring.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSItemProviderReading](../foundation/nsitemproviderreading.md)
- [NSItemProviderWriting](../foundation/nsitemproviderwriting.md)
- [NSMutableCopying](../foundation/nsmutablecopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class CSSearchableItem](cssearchableitem.md)
  The details of your app-specific content that someone might search for on their devices.
- [class CSSearchableItemAttributeSet](cssearchableitemattributeset.md)
  The detailed metadata for a searchable item.
- [class CSCustomAttributeKey](cscustomattributekey.md)
  A key associated with a custom attribute for a searchable item.
- [class CSPerson](csperson.md)
  An object that represents a person in the context of search results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cslocalizedstring)*