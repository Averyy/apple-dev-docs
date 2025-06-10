# requestAccess(for:completionHandler:)

**Framework**: Contacts  
**Kind**: method

Requests access to the user’s contacts.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func requestAccess(for entityType: CNEntityType) async throws -> Bool
```

## Mentions

- [Accessing the contact store](accessing-the-contact-store.md)

#### Discussion

> ❗ **Important**: You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func requestAccess(for entityType: CNEntityType) async throws -> Bool
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Users grant or deny access to contact data on a per-app basis. Request access to contact data by calling the [`requestAccess(for:completionHandler:)`](cncontactstore/requestaccess(for:completionhandler:).md) method, which returns right away. The first time your app calls this method, the system prompts the user to grant or deny access to your app. The system then saves the user’s response and does not prompt them again.

The system executes `completionHandler` on an arbitrary queue. It is recommended that you use [`CNContactStore`](cncontactstore.md) instance methods in this completion handler instead of the UI main thread. This method is optional when [`CNContactStore`](cncontactstore.md) is used in the background thread. If you don’t request access, [`CNContactStore`](cncontactstore.md) may block your app while asking the user for access.

## Parameters

- `entityType`: Set to  .
- `completionHandler`: Set granted to   if the user allows access and error is  .

## See Also

- [class func authorizationStatus(for: CNEntityType) -> CNAuthorizationStatus](cncontactstore/authorizationstatus(for:).md)
  Returns the current authorization status to access the contact data.
- [enum CNAuthorizationStatus](cnauthorizationstatus.md)
  An authorization status the user can grant for an app to access the specified entity type.
- [enum CNEntityType](cnentitytype.md)
  The entities the user can grant access to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontactstore/requestaccess(for:completionhandler:))*