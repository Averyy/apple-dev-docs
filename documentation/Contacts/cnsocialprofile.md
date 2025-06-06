# CNSocialProfile

**Framework**: Contacts  
**Kind**: class

An immutable object that represents one of the user’s social profiles.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CNSocialProfile
```

#### Overview

Some social profile services, such as Facebook and Twitter, are predefined in this class. You can also specify your own social profile service with the [`init(urlString:username:userIdentifier:service:)`](cnsocialprofile/init(urlstring:username:useridentifier:service:).md) method.

`CNSocialProfile` objects are thread-safe, and you may access their properties from any thread of your app.

## Topics

### Creating a Social Profile Object
- [init(urlString: String?, username: String?, userIdentifier: String?, service: String?)](cnsocialprofile/init(urlstring:username:useridentifier:service:).md)
  Initializes a new social profile object with the specified URL.
### Getting Social Profile Information
- [var username: String](cnsocialprofile/username.md)
  The user name for the social profile.
- [var service: String](cnsocialprofile/service.md)
  The social profile’s service name.
- [var urlString: String](cnsocialprofile/urlstring.md)
  The URL associated with the social profile.
- [var userIdentifier: String](cnsocialprofile/useridentifier.md)
  The service’s user identifier associated with the social profile.
### Getting Localized User Profile Information
- [class func localizedString(forKey: String) -> String](cnsocialprofile/localizedstring(forkey:).md)
  Returns the localized name of the property for the specified key.
- [let CNSocialProfileUsernameKey: String](cnsocialprofileusernamekey.md)
  The social profile user name.
- [let CNSocialProfileServiceKey: String](cnsocialprofileservicekey.md)
  The social profile service.
- [let CNSocialProfileURLStringKey: String](cnsocialprofileurlstringkey.md)
  The social profile URL.
- [let CNSocialProfileUserIdentifierKey: String](cnsocialprofileuseridentifierkey.md)
  The social profile user identifier.
### Getting Localized Service Names
- [class func localizedString(forService: String) -> String](cnsocialprofile/localizedstring(forservice:).md)
  Returns the localized name of the specified service.
- [let CNSocialProfileServiceFacebook: String](cnsocialprofileservicefacebook.md)
  The Facebook social profile service.
- [let CNSocialProfileServiceFlickr: String](cnsocialprofileserviceflickr.md)
  The Flickr social profile service.
- [let CNSocialProfileServiceGameCenter: String](cnsocialprofileservicegamecenter.md)
  The Game Center social profile service.
- [let CNSocialProfileServiceLinkedIn: String](cnsocialprofileservicelinkedin.md)
  The LinkedIn social profile service.
- [let CNSocialProfileServiceMySpace: String](cnsocialprofileservicemyspace.md)
  The MySpace social profile service.
- [let CNSocialProfileServiceSinaWeibo: String](cnsocialprofileservicesinaweibo.md)
  The Sina Weibo social profile service.
- [let CNSocialProfileServiceTencentWeibo: String](cnsocialprofileservicetencentweibo.md)
  The Tencent Weibo social profile service.
- [let CNSocialProfileServiceTwitter: String](cnsocialprofileservicetwitter.md)
  The Twitter social profile service.
- [let CNSocialProfileServiceYelp: String](cnsocialprofileserviceyelp.md)
  The Yelp social profile service.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cnsocialprofile)*