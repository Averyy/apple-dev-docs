# credentialForTrust:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates a URL credential instance for server trust authentication with a given accepted trust.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (NSURLCredential *) credentialForTrust:(SecTrustRef) trust;
```

## Return Value

A new URL credential object, containing the accepted server trust.

## Discussion

Before creating a server trust credential, it is the responsibility of the delegate of an [`NSURLConnection`](../nsurlconnection.md) instance or an [`NSURLDownload`](../nsurldownload.md) instance to evaluate the trust. Do this by calling `SecTrustEvaluate`, passing it the trust obtained from the `serverTrust` method of the server’s [`URLProtectionSpace`](../urlprotectionspace.md) instance. If the trust is invalid, the authentication challenge should be cancelled with the [`URLAuthenticationChallengeSender`](../urlauthenticationchallengesender.md) protocol’s `cancelAuthenticationChallenge:` method.

## Parameters

- `trust`: The accepted trust.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlcredential/credentialfortrust:)*