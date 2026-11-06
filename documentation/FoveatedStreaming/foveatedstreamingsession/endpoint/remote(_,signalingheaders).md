# remote(_:signalingHeaders:)

**Framework**: Foveated Streaming  
**Kind**: method  
**Role**: Type Method

Connects to a remote endpoint at a specific URL.

**Availability**:
- visionOS 27.3+ (Beta)

## Declaration

```swift
static func remote(_ url: URL, signalingHeaders: [String : String]) -> FoveatedStreamingSession.Endpoint
```

## Discussion

Use this when your app learns the endpoint at runtime — for example from your own control plane, which assigns a session host from a pool.

The system connects only if `url` is authorized by an entry in your app’s [`ApprovedStreamingEndpoints`](../../../BundleResources/information-property-list/approvedstreamingendpoints.md) dictionary in `Info.plist`.  An entry either names a single host, such as `edge1.example.com`, or names a set of subdomains with a leading-label wildcard, such as `*.example.com`.

A wildcard entry authorizes its domain and any subdomain of it, at any depth: `*.example.com` authorizes `example.com`, `edge1.example.com`, and `edge1.us-west.example.com`.  This is the same rule the system applies to the [Supporting associated domains](../../../Xcode/supporting-associated-domains.md) entitlement.  An entry that specifies no port authorizes any port; add a port to the entry, as in `*.example.com:8443`, to authorize only that one.

```swift
// A session host your control plane assigned, authorized by
// an "*.example.com" entry in ApprovedStreamingEndpoints.
let url = URL(string: "https://session-a7f3.us-west.example.com")!
try await session.connect(endpoint: .remote(url, signalingHeaders: ["Authorization": "Bearer \(token)"]))
```

## Parameters

- `url`: The URL of the remote streaming endpoint.
- `signalingHeaders`: HTTP headers which are forwarded to the remote server.  Use these headers for authentication and session management.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/endpoint/remote(_:signalingheaders:))*