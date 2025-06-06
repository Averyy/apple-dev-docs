# GSS

**Framework**: GSS  
**Kind**: module

Conduct secure, authenticated network transactions.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- visionOS 1.0+

#### Overview

The open source Generic Security Service Application Programming Interface (GSS-API) defines a standardized interface through which the operating system vends secure data transport operations. The GSS framework provides an implementation of the interface and the underlying libraries.

Using GSS-API, you can:

- Create a security context in which data can be passed between applications. A  represents a “state of trust” between two applications. Applications that share a context recognize each other and permit data transfers as long as the context lasts.
- Apply one or more types of protection, known as , to the data to be transmitted. For more on security services, see [`Security`](https://developer.apple.com/documentation/Security).
- Perform data conversion, error-checking, delegation of user privileges, information display, and identity comparison.

See [`RFC 2743`](https://developer.apple.comhttps://tools.ietf.org/html/rfc2743) for the definitive description of the GSS-API 2, and [`RFC 2744`](https://developer.apple.comhttps://tools.ietf.org/html/rfc2744) for a description of the related C bindings.

## Topics

### Memory and Context
- [Allocating and Releasing Objects](allocating-and-releasing-objects.md)
  Manage memory and object lifetimes.
- [Function Status](function-status.md)
  Evaluate return values that most GSS-API functions use to indicate the outcome of an operation.
- [Buffer Management](buffer-management.md)
  Allocate and deallocate buffers with structures that hold a variety of data.
- [Context Services](context-services.md)
  Use context services to manage secure operations between endpoints.
### Credentials
- [Credential Management](credential-management.md)
  Securely establish connections between endpoints.
- [Security Mechanisms](security-mechanisms.md)
  Provide a security mechanism for your implementation.
### Names and Object Identifiers
- [Name Handling](name-handling.md)
  Manage names for GSS-API principals such as a person, a machine, or an application.
- [Object Identifiers](object-identifiers.md)
  Store security mechanisms, QOPs (Quality of Protection values), and name types.
### Messages
- [Token Management](token-management.md)
  Establish secure communication with tokens.
- [Message Protection](message-protection.md)
  Provide cryptographic protection to secure message integrity.
- [Kerberos Implementation](kerberos-implementation.md)
  Establish secure connections using the Kerberos implementation of GSS-API.
### Structure and macros
- [Structures and macros](structures-and-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/GSS)*