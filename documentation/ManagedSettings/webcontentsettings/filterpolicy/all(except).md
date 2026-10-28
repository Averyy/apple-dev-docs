# WebContentSettings.FilterPolicy.all(except:)

**Framework**: Managed Settings  
**Kind**: case  
**Role**: Case

The system blocks all websites except the ones you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
case all(except: Set<WebDomain> = [])
```

## Discussion

Your app can specify up to 50 web domains exceptions.

## See Also

### Providing filters and exceptions
- [case auto(Set<WebDomain>, except: Set<WebDomain>)](./auto%28_,except%29.md)
  The system blocks adult content.
- [WebContentSettings.FilterPolicy.none](./none.md)
  The policy doesn’t affect any domains.
- [WebContentSettings.FilterPolicy.specific(_:)](./specific%28_%29.md)
  The policy blocks the specified domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webcontentsettings/filterpolicy/all(except:))*