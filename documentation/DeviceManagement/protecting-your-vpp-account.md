# Protecting Your VPP Account

**Framework**: Device Management

Ensure a Volume Purchase Program (VPP) account is not managed or reset by another product.

#### Overview

When first configuring a VPP account, the account might be reset by retiring all users and revoking all app assignments. Therefore, it is very important that your product always sets the `clientContext` data as documented below, so other products that manage VPP accounts can see that the VPP account is being managed by another product and not reset the VPP account without warning.

##### Vpp Account Protection

To ensure that a VPP account is not being managed by another product, follow these steps:

1. During initial setup, check the `clientContext` value returned from the [`Client Configuration`](client-configuration.md) endpoint. Create a JSON string with these keys and values: `{"hostname":<my.servername.com>, "guid":<random_uuid>}` The `guid` should be a standard 8-4-4-4-12 formatted UUID string and must be unique for each installation of your product. Write this JSON string to `clientContext` to claim this VPP account for your product. If the `clientContext` is not empty and does not match the `guid` value of your product, report the `hostname` returned by `clientContext` and confirm that your product should take over from it. Do not rely on `hostname` to confirm that your product still has a proper claim on the VPP account.
2. At the start of  subsequent VPP session, check `clientContext` to ensure that it still represents the correct installation of your product.
3. If `clientContext` no longer refers to your product, do not make any further requests to the VPP service for that VPP account until the account has been reactivated by administrator commands. Your product should report this isolation action to an administrator, giving the `hostname` of the server that now claims to manage the VPP account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/protecting-your-vpp-account)*