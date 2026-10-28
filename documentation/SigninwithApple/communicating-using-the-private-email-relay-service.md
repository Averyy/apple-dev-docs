# Communicating using the private email relay service

**Framework**: Sign in with Apple  
**Role**: Article

Stay in touch with users who opt for an anonymous email address with Sign in with Apple.

## Overview

People who communicate with you about your app may choose to protect their private email information. To facilitate communication between users and developers, Sign in with Apple gives users the ability to use an anonymous email address. When a user provides such an address to your app, the *private relay email service* routes all emails between you and the user. A private relay email service sends email to a recipient using an automatically generated email address. This hides the real email address to preserve privacy.

Private relay email addresses have the following characteristics:

- They end in `@private.icloud.com`, `@privaterelay.appleid.com`, or `@icloud.com`.
- They route emails to one of the Apple Account’s verified email addresses.
- They’re the same for a user across all apps written by a single development team, and different for the same user across apps written by different development teams.
- They’re active whether or not the user is signed into a device, and whether or not your app is installed on the device. You may send and receive email to the private email address at any time.

After the user has shared a private relay email address with your app, they can find, view, and manage it in their account settings at Settings > Sign in with Apple > Apps and Websites.

> ❗ **Important**:  Each private relay email address has a daily limit of 100 emails, which includes emails from the developer to the relay address, as well as user replies.

The following sequence chart shows how the private email relay service works:

![A sequence diagram that describes how a user sends and receives an email through the private email relay service. At the top of the diagram are five actors, including: Developer Mail Client, Developer Mail Transfer Agent, Private Relay Mail Transfer Client, User Mail Transfer Client, and User Mail Client. The steps of the private email relay service are illustrated in the diagram with horizontal arrows across the actors’ lifelines, beginning with Submit email and ending with Receive reply.](https://developer.apple.com/tutorials/images/com.apple.signinwithapple/media-3385259@2x.png)

### Register Your Email Domain

To send emails to users with private email addresses, you must register your outbound emails or email domains and use Sender Policy Framework (SPF) to authenticate your outbound emails. These mechanisms ensure that only you can communicate with your users through this channel, and they prevent spam from getting through.

### Send and Receive Emails

After you register your outbound email domains, you can send emails to users through the private email relay service. When they reply, the relay server routes the replies back to the email address used in your original email. To enable this functionality, the relay server transforms your email address so it’s readable to the user. For example, `sales@example.com` may become `sales_at_example_com_<something>@icloud.com` instead of a random email address. Replies from the user continue to route back through the service to preserve the user’s privacy.

If a user chooses to stop receiving email from your app, the relay server rejects all future emails sent to that address. Because the address is the same for all apps written by a development team, disabling the relay service informs the user of all other affected apps.

## See Also

### Essentials
- [Configuring your webpage for Sign in with Apple](./configuring-your-webpage-for-sign-in-with-apple.md)
  Prepare your webpage to authorize users through Sign in with Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/signinwithapple/communicating-using-the-private-email-relay-service)*