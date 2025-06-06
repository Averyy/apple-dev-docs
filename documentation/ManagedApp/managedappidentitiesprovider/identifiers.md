# identifiers

**Framework**: ManagedApp  
**Kind**: property

An asynchronous sequence of arrays of identity identifiers provided by the MDM server.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- visionOS 2.4+

## Declaration

```swift
var identifiers: some AsyncSequence<Array<String>, Never> { get async }
```

#### Discussion

Use [`identity(withIdentifier:)`](managedappidentitiesprovider/identity(withidentifier:).md) to look up an identifier to obtain the associated identity. The sequence yields an array of identifiers when:

- You begin iterating this property using `for await`.
- The list of identity identifiers changes.
- The value of one or more identities changes.

You define the values of the identifiers that an MDM admin can use. Define specific individual values or ranges of values to group identities, or use the configuration to determine the meaning of the identifiers.

This property yields an empty array if the MDM admin hasn’t provisioned any identities for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedapp/managedappidentitiesprovider/identifiers)*