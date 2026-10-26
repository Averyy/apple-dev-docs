# NSURLHandle

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object that accesses and manages resource data indicated by a URL.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSURLHandle
```

```objc
@interface NSURLHandle : NSObject
```

#### Overview

> ❗ **Important**:  [`NSURLHandle`](./nsurlhandle.md) is deprecated in macOS 10.4 and later. Use [`URLSession`](./urlsession.md) instead.

A single [`NSURLHandle`](./nsurlhandle.md) can service multiple equivalent [`NSURL`](./nsurl.md) objects, but only if these URLs map to the same resource.

##### Overview

Cocoa provides private concrete subclasses to handle HTTP and file URL schemes. If you want to implement support for additional URL schemes, you would do so by creating a subclass of `NSURLHandle`. You can use `NSURL` and `NSURLHandle` to download from FTP sites without subclassing.

## Topics

### Loading resource data
- [NSURLHandle.Status](./nsurlhandle/status-swift.enum.md)
  These following constants are defined by `NSURLHandle` and are returned by [`status`](./nsurlhandle/status-c.method.md).
- [- availableResourceData](./nsurlhandle/availableresourcedata.md)
  Immediately returns the currently available resource data managed by the URL handle.
- [- backgroundLoadDidFailWithReason:](./nsurlhandle/backgroundloaddidfailwithreason_.md)
  Called when a background load fails.
- [- beginLoadInBackground](./nsurlhandle/beginloadinbackground.md)
  Called when a background load begins.
- [- cancelLoadInBackground](./nsurlhandle/cancelloadinbackground.md)
  Called to cancel a load currently in progress.
- [- didLoadBytes:loadComplete:](./nsurlhandle/didloadbytes_loadcomplete_.md)
  Appends new data to the receiver’s resource data.
- [- endLoadInBackground](./nsurlhandle/endloadinbackground.md)
  Halts any background loading.
- [- expectedResourceDataSize](./nsurlhandle/expectedresourcedatasize.md)
  Returns the expected length of the resource data if it is provided by the server.
- [- failureReason](./nsurlhandle/failurereason.md)
  Returns a string describing the reason a load failed.
- [- flushCachedData](./nsurlhandle/flushcacheddata.md)
  Flushes any cached data for the URL served by this URL handle.
- [- loadInBackground](./nsurlhandle/loadinbackground.md)
  Loads the receiver’s data in the background.
- [- loadInForeground](./nsurlhandle/loadinforeground.md)
  Loads the receiver’s data synchronously.
- [- resourceData](./nsurlhandle/resourcedata.md)
  Returns the resource data managed by the receiver, loading it if necessary.
- [- status](./nsurlhandle/status-c.method.md)
  Returns the status of the receiver.
### Constructing NSURLHandles
- [+ cachedHandleForURL:](./nsurlhandle/cachedhandleforurl_.md)
  Returns the URL handle from the cache that has serviced the specified URL or another identical URL.
- [- initWithURL:cached:](./nsurlhandle/initwithurl_cached_.md)
  Initializes a newly created URL handle with the specified URL.
### Managing subclasses
- [+ URLHandleClassForURL:](./nsurlhandle/urlhandleclassforurl_.md)
  Returns the class of the URL handle that will be used for a specified URL.
- [+ canInitWithURL:](./nsurlhandle/caninitwithurl_.md)
  Returns whether a URL handle can be initialized with a given URL.
- [+ registerURLHandleClass:](./nsurlhandle/registerurlhandleclass_.md)
  Registers a subclass of `NSURLHandle` as an available subclass for handling URLs
### Managing clients
- [- addClient:](./nsurlhandle/addclient_.md)
  Adds a client of the URL handle.
- [- removeClient:](./nsurlhandle/removeclient_.md)
  Removes `client` as an `NSURLHandleClient` of the receiver.
### Setting and getting resource properties
- [- propertyForKey:](./nsurlhandle/propertyforkey_.md)
  Returns the property for the specified key.
- [- propertyForKeyIfAvailable:](./nsurlhandle/propertyforkeyifavailable_.md)
  Returns the property for the specified key only if the value is already available; that is, the client doesn’t need to do any work.
- [- writeProperty:forKey:](./nsurlhandle/writeproperty_forkey_.md)
  Sets the property of the receiver’s resource for a specified key to the specified value.
### Writing resource data
- [- writeData:](./nsurlhandle/writedata_.md)
  Attempts to write a specified set of data to the location specified by the receiver’s URL.
### Resource Property Keys
- [NSFTPPropertyActiveTransferModeKey](./nsftppropertyactivetransfermodekey.md)
  Key for retrieving whether in active transfer mode, returned as a boolean wrapped in an `NSNumber` object.
- [NSFTPPropertyFTPProxy](./nsftppropertyftpproxy.md)
  `NSDictionary` containing proxy information to use in place of proxy identified in `SystemConfiguration.framework`.
- [NSFTPPropertyFileOffsetKey](./nsftppropertyfileoffsetkey.md)
  Key for retrieving the file offset, returned as an `NSNumber` object. The default value for this key is zero.
- [NSFTPPropertyUserLoginKey](./nsftppropertyuserloginkey.md)
  Key for the user login, returned as an `NSString` object.
- [NSFTPPropertyUserPasswordKey](./nsftppropertyuserpasswordkey.md)
  Key for the user password, returned as an `NSString` object.
- [NSHTTPPropertyErrorPageDataKey](./nshttppropertyerrorpagedatakey.md)
  Key for retrieving an error page as an `NSData` object.
- [NSHTTPPropertyHTTPProxy](./nshttppropertyhttpproxy.md)
  Key for retrieving the `NSDictionary` object containing proxy information to use in place of proxy identified in `SystemConfiguration.framework`.
- [NSHTTPPropertyRedirectionHeadersKey](./nshttppropertyredirectionheaderskey.md)
  Key for retrieving the redirection headers as an `NSDictionary` object with each header value keyed to the header name.
- [NSHTTPPropertyServerHTTPVersionKey](./nshttppropertyserverhttpversionkey.md)
  Key for retrieving the HTTP version as an `NSString` object containing the initial server status line up to the first space.
- [NSHTTPPropertyStatusCodeKey](./nshttppropertystatuscodekey.md)
  Key for the status code, returned as an integer wrapped in an `NSNumber` object.
- [NSHTTPPropertyStatusReasonKey](./nshttppropertystatusreasonkey.md)
  Key for the remainder of the HTTP status line following the status code, returned as an `NSString` object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### URL Handle
- [NSURLHandleClient](./nsurlhandleclient.md)
  The interface implemented by URL handle clients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle)*